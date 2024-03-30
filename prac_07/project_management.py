from project import Project
import datetime


def load_projects():
    projects = []
    with open("projects.txt", 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split('\t')
            project = Project(*data)
            projects.append(project)
    return projects


def save_projects(projects):
    with open("projects.txt", 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.percent_complete}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if int(project.percent_complete) < 100]
    completed_projects = [project for project in projects if int(project.percent_complete) == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: int(x.priority)):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(completed_projects, key=lambda x: int(x.priority)):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.is_after_date(date)]

    print("Filtered projects:")
    for project in sorted(filtered_projects, key=lambda x: datetime.datetime.strptime(x.start_date, "%d/%m/%Y")):
        print(f"  {project}")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")

    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]
    print(selected_project)

    percent_complete = input("New Percentage: ")
    priority = input("New Priority: ")
    selected_project.update_project(percent_complete, priority)


if __name__ == "__main__":
    file_name = "projects.txt"
    projects = load_projects()

    while True:
        print("""
        - (L)oad projects  
        - (S)ave projects  
        - (D)isplay projects  
        - (F)ilter projects by date
        - (A)dd new project  
        - (U)pdate project
        - (Q)uit
        """)

        choice = input(">>> ").lower()

        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects()
        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects(projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select a valid option.")