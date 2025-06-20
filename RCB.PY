import psycopg2

# Connect to DB
conn = psycopg2.connect(
    host="localhost",
    database="RCB_DB",        # ✅ Your actual DB name
    user="postgres",          # ✅ Your PostgreSQL username
    password="8484"           # ✅ Your PostgreSQL password
)
cur = conn.cursor()

# Search player in DB
def get_player(player_jersey):
    cur.execute("SELECT * FROM players WHERE player_jersey = %s", (player_jersey,))
    return cur.fetchone()

# Add new player
def add_player(player_jersey):
    name = input("Enter name: ")
    role = input("Enter role: ")
    runs = int(input("Enter runs: "))
    strike_rate = float(input("Enter strike rate: "))

    cur.execute(
        "INSERT INTO players (player_jersey, name, role, runs, strike_rate) VALUES (%s, %s, %s, %s, %s)",
        (player_jersey, name, role, runs, strike_rate)
    )
    conn.commit()
    print("✅ New player added to the database!")

# Main logic
player_jersey = input("Enter player jersey number: ").strip()

player = get_player(player_jersey)

if player:
    print(f"""
👤 Player Found:
Jersey No   : {player[0]}
Name        : {player[1]}
Role        : {player[2]}
Runs        : {player[3]}
Strike Rate : {player[4]}
""")
else:
    print("❌ Player not found.")
    add = input("Do you want to add this player? (yes/no): ").lower()
    if add == "yes":
        add_player(player_jersey)

# Close connection
cur.close()
conn.close()
