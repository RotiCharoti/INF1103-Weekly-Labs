class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def get_supplier_id(self) -> str:
        return self.supplier_id
    
    def get_supplier_name(self) -> str: 
        return self.name
    
    def get_supplier_contact_email(self) -> str:
        return self.contact_email
    
    def display_information(self) -> str:
        return f"Supplier ID: {self.supplier_id}, Supplier Name: {self.name}, Contact Info: {self.contact_email}"