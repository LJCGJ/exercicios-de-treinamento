## Purpose

Define as regras de comportamento do catálogo de produtos de um e-commerce, garantindo que administradores possam gerenciar itens do catálogo de forma consistente, segura e testável.

## ADDED Requirements

### Requirement: Product catalog supports product creation
The system SHALL allow administrators to create a new product with a unique identifier, name, description, price, and stock quantity.

#### Scenario: Product created successfully
- **WHEN** an administrator submits valid product data
- **THEN** the system creates the product and returns a successful response with the created product details

#### Scenario: Product creation with invalid data
- **WHEN** an administrator submits product data missing required fields or with invalid values
- **THEN** the system rejects the request and returns a validation error

### Requirement: Product catalog supports product listing
The system SHALL allow administrators to list all available products in the catalog and retrieve a specific product by identifier.

#### Scenario: Listing all products
- **WHEN** an administrator requests the catalog
- **THEN** the system returns the list of products in the catalog

#### Scenario: Retrieving a product by ID
- **WHEN** an administrator requests an existing product by identifier
- **THEN** the system returns the product details

#### Scenario: Product not found
- **WHEN** an administrator requests a product identifier that does not exist
- **THEN** the system returns a not found error

### Requirement: Product catalog supports product update
The system SHALL allow administrators to update product information for an existing product.

#### Scenario: Updating product details
- **WHEN** an administrator submits valid changes for an existing product
- **THEN** the system updates the product and returns the updated data

#### Scenario: Updating a non-existent product
- **WHEN** an administrator tries to update a product that does not exist
- **THEN** the system returns a not found error

### Requirement: Product catalog supports product deletion
The system SHALL allow administrators to remove a product from the catalog.

#### Scenario: Deleting an existing product
- **WHEN** an administrator requests deletion for an existing product
- **THEN** the system removes the product and confirms the operation

#### Scenario: Deleting a non-existent product
- **WHEN** an administrator requests deletion for a missing product
- **THEN** the system returns a not found error
