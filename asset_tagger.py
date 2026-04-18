from datetime import datetime

analyst_name = input("Enter your name: ")
department = input("Enter department: ")
system_name = input("Enter system hostname: ")
criticality = input("Enter system criticality (low, medium, high): ")
risk_score = int(input("Enter a risk score (1-10): "))

if risk_score >= 8:
    assessment = "High-Risk Asset – prioritize review."
elif risk_score >= 5:
    assessment = "Medium-Risk Asset – monitor closely."
else:
    assessment = "Low-Risk Asset – standard monitoring."

print("\n" + "="*40)
print("     Cyber Defense - Asset Report")
print("="*40)
print(f"Analyst: {analyst_name}")
print(f"Department: {department}")
print(f"Hostname: {system_name}")
print(f"Criticality: {criticality}")
print(f"Risk Score: {risk_score}")
print(f"Risk Assessment: {assessment}")
print(f"Report Generated: {datetime.now()}")
print("="*40)