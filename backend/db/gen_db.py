#Database Creation and configuration script to be modified and completed

import sqlite3
import os
from datetime import datetime


rewrite = False

# Name of the database file
DB_NAME = "database.db"

if os.path.isfile(DB_NAME):

    last_modified = os.path.getmtime(DB_NAME)
    #convert to datetime
    last_modified = datetime.fromtimestamp(last_modified)

    ans =  input(f"Database already exists (Last modification on {last_modified} ). Do you want to rewrite it? (y/N) \n> ")
    rewrite = (ans == "y" or ans == "Y")


# if the file does not exist,or we want to rewrite it:
if (not os.path.isfile(DB_NAME)) or rewrite:
    print("Creating database file...")
    open(DB_NAME, "w").close()

    # Connect to the database
    try:
        conn = sqlite3.connect(DB_NAME)
        print("\33[92mConnected to database\33[0m")
        c = conn.cursor()
    except sqlite3.Error as e:
        print("\33[91mCould not connect to database\33[0m",e)
        exit()

    #Enable foreign keys
    c.execute("PRAGMA foreign_keys = ON")

    # Create cheques table
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS cheques (
            cqID INTEGER PRIMARY KEY AUTOINCREMENT,
            banque STRING, 
            dateEmis DATE, 
            raisonSociale STRING, 
            noCheque STRING,
            dateEncaissement DATE,
            montant FLOAT,
            versement_ccp STRING,
            dateVersement DATE,
            datePrelevement DATE
            )
        ''')
        print("\33[92mCreated cheques table\33[0m")
    except sqlite3.Error as e:
        print(f"Failed to create cheques Table\nQuery execution: \33[91merror\33[0m\n -> {e} \n Resulting DB may be corrupted \n Quitting...")
        exit()

    conn.commit()

    # Create creances_fournisseur_Importants table
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS creances_fournisseur_Importants (
            crID INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE, 
            raisonSociale STRING, 
            noFacture STRING,
            montant FLOAT,
            datePaiement DATE,
            noCheque STRING,
            remarques_banque STRING
            )
        ''')
        print("\33[92mCreated creances_fournisseur_Importants table\33[0m")
    except sqlite3.Error as e:
        print(f"Failed to create creances_fournisseur_Importants Table\nQuery execution: \33[91merror\33[0m\n -> {e} \n Resulting DB may be corrupted \n Quitting...")
        exit()

    conn.commit()

    # Create creances_fournisseur_GROS_COMPTES table
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS creances_fournisseur_GROS_COMPTES (
            crID INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE, 
            raisonSociale STRING, 
            noFacture STRING,
            montant FLOAT,
            datePaiement DATE,
            noCheque STRING,
            remarques_banque STRING
            )
        ''')
        print("\33[92mCreated creances_fournisseur_GROS_COMPTES table\33[0m")
    except sqlite3.Error as e:
        print(f"Failed to create creances_fournisseur_GROS_COMPTES Table\nQuery execution: \33[91merror\33[0m\n -> {e} \n Resulting DB may be corrupted \n Quitting...")
        exit()

    conn.commit()

        # Create creances_fournisseur_GROS_divers table
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS creances_fournisseur_GROS_divers (
            crID INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE, 
            raisonSociale STRING, 
            noFacture STRING,
            montant FLOAT,
            datePaiement DATE,
            noCheque STRING,
            remarques_banque STRING
            )
        ''')
        print("\33[92mCreated creances_fournisseur_GROS_divers table\33[0m")
    except sqlite3.Error as e:
        print(f"Failed to create creances_fournisseur_GROS_divers Table\nQuery execution: \33[91merror\33[0m\n -> {e} \n Resulting DB may be corrupted \n Quitting...")
        exit()

    conn.commit()


    # Close connection
    conn.close()
    print("\33[1mALL DONE GOING BACK TO SLEEP NOW\33[0m")



