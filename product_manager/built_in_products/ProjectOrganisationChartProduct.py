"""Project organisation chart product stub."""

from ..Product import Product


class ProjectOrganisationChartProduct(Product):
    """Represents a project organisation chart."""

    def __init__(self):
        super().__init__(
            name="ProjectOrganisationChartProduct",
            description="Visual depiction of project roles and reporting lines.",
        )

    def draft(self):  # pragma: no cover - minimal stub
        """Draft the organisation chart."""
        pass

    def review(self):  # pragma: no cover - minimal stub
        """Review the organisation chart."""
        pass

    def complete(self):  # pragma: no cover - minimal stub
        """Finalize the organisation chart."""
        pass

    def export(self):  # pragma: no cover - minimal stub
        """Export the chart."""
        pass

