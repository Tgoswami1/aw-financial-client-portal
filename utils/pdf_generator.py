from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    client_name,
    report_date,
    savings_target,
    net_worth,
    private_reserve,
    investment_balance,
    trust_value,
    liabilities
):

    filename = f"{client_name}_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "AW Financial Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Client: {client_name}",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Date: {report_date}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Savings Target: ${savings_target:,.0f}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Net Worth: ${net_worth:,.0f}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Private Reserve: ${private_reserve:,.0f}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Investment Balance: ${investment_balance:,.0f}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Trust Value: ${trust_value:,.0f}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Liabilities: ${liabilities:,.0f}",
            styles["Normal"]
        )
    )

    doc.build(story)

    return filename