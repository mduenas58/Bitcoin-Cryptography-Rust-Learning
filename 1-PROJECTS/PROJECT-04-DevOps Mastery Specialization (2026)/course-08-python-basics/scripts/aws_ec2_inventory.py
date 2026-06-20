#\!/usr/bin/env python3
"""
Dynamic EC2 inventory script using boto3.
Lists running instances with Name, IP, and type.
"""
import boto3
from rich.console import Console
from rich.table import Table

console = Console()


def list_instances(region: str = "us-east-1"):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    table = Table(title=f"Running EC2 Instances — {region}", show_lines=True)
    table.add_column("Name",         style="cyan")
    table.add_column("Instance ID",  style="magenta")
    table.add_column("Type")
    table.add_column("Private IP",   style="green")
    table.add_column("Public IP",    style="yellow")

    for reservation in response["Reservations"]:
        for inst in reservation["Instances"]:
            name = next(
                (t["Value"] for t in inst.get("Tags", []) if t["Key"] == "Name"),
                "—",
            )
            table.add_row(
                name,
                inst["InstanceId"],
                inst["InstanceType"],
                inst.get("PrivateIpAddress", "—"),
                inst.get("PublicIpAddress", "—"),
            )

    console.print(table)


if __name__ == "__main__":
    list_instances()
