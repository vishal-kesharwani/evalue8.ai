from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.routing_trace import RoutingTraceEntry
from app.schemas.analytics import AnalyticsSummary, DomainCost, ModelCost, ModelCount


class TraceService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def record(self, **fields) -> RoutingTraceEntry:
        entry = RoutingTraceEntry(**fields)
        self.db.add(entry)
        await self.db.commit()
        await self.db.refresh(entry)
        return entry

    async def list_traces(
        self,
        model: str | None = None,
        domain: str | None = None,
        outcome: str | None = None,
        limit: int = 100,
    ) -> list[RoutingTraceEntry]:
        query = select(RoutingTraceEntry).order_by(RoutingTraceEntry.timestamp.desc()).limit(limit)
        if model:
            query = query.where(RoutingTraceEntry.selected_model == model)
        if domain:
            query = query.where(RoutingTraceEntry.task_domain == domain)
        if outcome:
            query = query.where(RoutingTraceEntry.outcome == outcome)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def analytics_summary(self) -> AnalyticsSummary:
        total = await self.db.scalar(select(func.count()).select_from(RoutingTraceEntry))

        by_model = await self.db.execute(
            select(RoutingTraceEntry.selected_model, func.count()).group_by(RoutingTraceEntry.selected_model)
        )
        cost_by_model_rows = await self.db.execute(
            select(RoutingTraceEntry.selected_model, func.sum(RoutingTraceEntry.estimated_cost)).group_by(
                RoutingTraceEntry.selected_model
            )
        )
        cost_by_domain_rows = await self.db.execute(
            select(RoutingTraceEntry.task_domain, func.sum(RoutingTraceEntry.estimated_cost)).group_by(
                RoutingTraceEntry.task_domain
            )
        )

        return AnalyticsSummary(
            total_requests=total or 0,
            requests_by_model=[ModelCount(model=m, count=c) for m, c in by_model.all()],
            cost_by_model=[ModelCost(model=m, total_cost=round(c or 0, 6)) for m, c in cost_by_model_rows.all()],
            cost_by_domain=[DomainCost(domain=d, total_cost=round(c or 0, 6)) for d, c in cost_by_domain_rows.all()],
        )
