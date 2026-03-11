from agents.workflow import run_workflow


def main() -> None:
    print("=== Cloud Incident Triage Copilot ===")
    incident_text = input("\nEnter incident description:\n> ").strip()

    if not incident_text:
        print("No incident entered. Exiting.")
        return

    result = run_workflow(incident_text)

    print("\n=== FINAL INCIDENT BRIEF ===\n")
    print(result["final_output"])


if __name__ == "__main__":
    main()
