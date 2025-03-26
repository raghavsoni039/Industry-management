This program is a Metallurgy Industry Management System using Python and MySQL. It manages data related to ores, workers, and their financial information in a metallurgy industry. The system allows adding, updating, deleting, and displaying records in a structured manner.

Key Features:
Database & Table Management
Establishes a connection to MySQL and creates a database METALLURGY_INDUSTRY_MANAGEMENT.
Defines three tables:
            ORE (for storing ore details such as name, chemical formula, metal, and price).
            WORKERS (for managing worker details like ID, name, contact number, and department).
            FINANCIAL_INFO (for storing salary and worker ID references).

CRUD Operations:
            Functions for adding, deleting, updating, and displaying records in each table.

User Interaction Menus:    
            ORE_MENU(), WORKERS_MENU(), and FINANCIAL_MENU() provide structured interactions.
            MAIN_MENU() acts as the central navigation for different operations.

Uses primary keys and foreign key references.
Provides input validation with loops to prevent incorrect entries.
