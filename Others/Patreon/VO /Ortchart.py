ORG_CHART = {
    "John": {
        "Weston": None,
        "Jones": {
            "Paul": None
        }
    },
    "Lou": None
}

def get_num_of_indirect_reports(org_level):
    """Recursively counts the number of indirect reports"""
    if not org_level:
        return 0
    
    count = 0
    for employee_name, reports in org_level.items():
        if reports:
            count += get_num_of_indirect_reports(reports) + 1
    return count

def get_num_of_total_reports(org_level):
    """Recursively counts the number of indirect reports"""
    if not org_level:
        return 0
    
    count = 0
    for employee_name, reports in org_level.items():
        print(employee_name, reports)
        count += 1
        if reports:
            count += get_num_of_total_reports(reports)
    return count

print(get_num_of_indirect_reports(ORG_CHART["John"]))
print(get_num_of_total_reports(ORG_CHART["John"]))

def get_employee_info(employee_name, org_level):
    """Recursively searches for an employee and retrieves their information."""
    # Base case 1: No more levels to search
    if not org_level:
        return []
    
    # Base case 2: Found the employee
    if employee_name in org_level:
        if org_level[employee_name]:
            # Employee is a manager
            num_direct_reports = len(org_level[employee_name])
            num_indirect_reports = get_num_of_indirect_reports(org_level[employee_name])
            return [employee_name, "manager", num_direct_reports, num_direct_reports + num_indirect_reports]
        else:
            # Employee is an individual contributor (IC)
            return [employee_name, "ic", 0, 0]
    
    # Recursive case: Search nested levels
    for name, reports in org_level.items():
        result = get_employee_info(employee_name, reports)
        if result:
            return result
    
    return []

# Example usage
print(get_employee_info("Lou", ORG_CHART))  # Output: ['Lou', 'ic', 0, 0]
print(get_employee_info("John", ORG_CHART))  # Output: ['John', 'manager', 2, 3]