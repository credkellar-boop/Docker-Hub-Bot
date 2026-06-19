from tabulate import tabulate # Requires: pip install tabulate

def print_dashboard():
    data = [["Node", "Status"], ["DockerHub", "Connected"], ["LegalVault", "Locked"]]
    print(tabulate(data, headers="firstrow"))
