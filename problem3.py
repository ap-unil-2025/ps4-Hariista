"""
Problem 3: Mini Contact Manager
Build a simple contact manager using lists and dictionaries.
Practice combining data structures and writing functions.
"""


def create_contact(name, phone, email=""):
    """
    Create a contact dictionary.
    """
    return {
        "name": name,
        "phone": phone,
        "email": email
    }


def add_contact(contacts, name, phone, email=""):
    """
    Add a new contact to the contacts list.
    """
    contact = create_contact(name, phone, email)
    contacts.append(contact)
    return contact


def find_contact_by_name(contacts, name):
    """
    Find a contact by name (case-insensitive).
    """
    name_lower = name.lower()
    for contact in contacts:
        if contact["name"].lower() == name_lower:
            return contact
    return None


def search_contacts(contacts, search_term):
    """
    Search for contacts by name or phone (partial match).
    """
    search_term = search_term.lower()
    results = []

    for contact in contacts:
        if (search_term in contact["name"].lower()
                or search_term in contact["phone"].lower()):
            results.append(contact)

    return results


def delete_contact(contacts, name):
    """
    Delete a contact by name.
    """
    name_lower = name.lower()
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name_lower:
            contacts.pop(i)
            return True
    return False


def count_contacts_with_email(contacts):
    """
    Count how many contacts have an email address.
    """
    count = 0
    for contact in contacts:
        if contact["email"]:
            count += 1
    return count


def get_all_phone_numbers(contacts):
    """
    Extract all phone numbers from contacts.
    """
    return [contact["phone"] for contact in contacts]


def sort_contacts_by_name(contacts):
    """
    Return a new list of contacts sorted alphabetically by name.
    """
    return sorted(contacts, key=lambda c: c["name"])


def contact_exists(contacts, name):
    """
    Check if a contact with the given name exists.
    """
    return find_contact_by_name(contacts, name) is not None


# Test cases
if __name__ == "__main__":
    print("Testing Mini Contact Manager...")
    print("-" * 50)

    contacts = []

    print("Test 1: create_contact")
    contact = create_contact("Alice", "555-0001", "alice@email.com")
    assert contact == {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}
    print("✓ Passed\n")

    print("Test 2: add_contact")
    add_contact(contacts, "Alice", "555-0001", "alice@email.com")
    add_contact(contacts, "Bob", "555-0002")
    add_contact(contacts, "Charlie", "555-0003", "charlie@email.com")
    assert len(contacts) == 3
    print("✓ Passed\n")

    print("Test 3: find_contact_by_name")
    found = find_contact_by_name(contacts, "alice")
    assert found is not None and found["name"] == "Alice"
    print("✓ Passed\n")

    print("Test 4: search_contacts")
    results = search_contacts(contacts, "555-000")
    assert len(results) == 3
    print("✓ Passed\n")

    print("Test 5: count_contacts_with_email")
    assert count_contacts_with_email(contacts) == 2
    print("✓ Passed\n")

    print("Test 6: get_all_phone_numbers")
    phones = get_all_phone_numbers(contacts)
    assert phones == ["555-0001", "555-0002", "555-0003"]
    print("✓ Passed\n")

    print("Test 7: sort_contacts_by_name")
    sorted_contacts = sort_contacts_by_name(contacts)
    names = [c["name"] for c in sorted_contacts]
    assert names == ["Alice", "Bob", "Charlie"]
    print("✓ Passed\n")

    print("Test 8: contact_exists")
    assert contact_exists(contacts, "Alice") is True
    assert contact_exists(contacts, "David") is False
    print("✓ Passed\n")

    print("Test 9: delete_contact")
    deleted = delete_contact(contacts, "Bob")
    assert deleted is True and len(contacts) == 2
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work on the contact manager!")