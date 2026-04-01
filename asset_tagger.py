print("        ASSET TAGGER v1.0         ")

hostname = input("Enter the asset hostname: ")
criticality = input("Enter the asset criticality (Low, Medium, High): ")

risk_score_input = input("Enter the asset risk score (1-10): ")
risk_score = int(risk_score_input)

is_high_risk = False

if criticality.lower() == "high" or risk_score >= 8:
    is_high_risk = True

print("\n==================================")
print("        ASSET RISK REPORT         ")
print("==================================")
print(f"Hostname:    {hostname}")
print(f"Criticality: {criticality.capitalize()}")
print(f"Risk Score:  {risk_score}/10")

if is_high_risk:
    print("Status:      [!] HIGH RISK [!]")
else:
    print("Status:      [+] Acceptable Risk")
print("==================================")