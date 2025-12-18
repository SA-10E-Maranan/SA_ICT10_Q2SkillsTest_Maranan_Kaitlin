from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "plants": {
                "name": "Verdant Circle",
                "level": "Novice/Beginners",
                "description": "Casters learn the basics of magical plants and herbology.",
                "meeting_time": "Every Monday, 2:00 to 3:30 PM",
                "location": "The Sylvan Conservatory",
                "advisor": "Professor Thalia Greenroot",
                "members": 20,
                "category": "Academic"
            },
            "potions": {
                "name": "Crucible & Cauldron Society",
                "level": "Novice/Beginners",
                "description": "Casters focus on potion-making basics.",
                "meeting_time": "Every Monday, 3:30 to 5:00 PM",
                "location": "The Emberbrew Chamber",
                "advisor": "Professor Elorren Brasswick",
                "members": 24,
                "category": "Academic"
            },
            "brooms": {
                "name": "Broombornes",
                "level": "Novice/Beginners",
                "description": "Learn broom-riding, aerial teamwork, and 
                magical racing techniques.",
                "meeting_time": "Every Wednesday, 2:30 to 4:00 PM",
                "location": "The Skybound Rings",
                "advisor": "Coach Leon Galehart",
                "members": 32,
                "category": "Sports"
            },
            "music": {
                "name": "Harmonic Enchanters",
                "level": "Novice/Beginners",
                "description": "Magical music club; casters channel magic through sound.",
                "meeting_time": "Every Thursday, 2:00 to 3:30 PM",
                "location": "The Starveil Hall",
                "advisor": "Professor Zina Dawnveil",
                "members": 20,
                "category": "Arts"
            },
            "animals": {
                "name": "Creatures' Keepers",
                "level": "Novice/Beginners",
                "description": "Casters care for and bond with magical creatures.",
                "meeting_time": "Every Thursday, 3:15 to 4:30 PM",
                "location": "The Moonpetal Conservatory",
                "advisor": "Mistress Calla Fenwood",
                "members": 27,
                "category": "Arts"
            },
            "threads": {
                "name": "Glimmering Threads",
                "level": "Novice/Beginners",
                "description": "Beginner crafting with minor enchantments.",
                "meeting_time": "Every Tuesday, 3:45 to 5:00 PM",
                "location": "The Looming Room",
                "advisor": "Professor Kael Emberwind",
                "members": 20,
                "category": "Arts"
            },
            "conjure": {
                "name": "Miniature Conjurors",
                "level": "Novice/Beginners",
                "description": "Introductory summoning and control of small magical constructs or tiny creatures.",
                "meeting_time": "Every Wednesday, 2:00 to 3:30 PM",
                "location": "The Starveil Hall",
                "advisor": "Professor Liora Spellbind",
                "members": 16,
                "category": "Academic"
            },
            "dark": {
                "name": "Shadowmancy",
                "level": "Scholars/Advanced",
                "description": "Casters study shadow manipulation and dark magic.",
                "meeting_time": "Every Tuesday, 2:00 to 3:30 PM",
                "location": "The Obsidian Training Alcove",
                "advisor": "Professor Malrik Duskveil",
                "members": 16,
                "category": "Academic"
            },
            "light": {
                "name": "Radiant Conclave",
                "level": "Scholars/Advanced",
                "description": "Advanced light magic for advanced casters.",
                "meeting_time": "Every Tuesday, 3:45 to 5:00 PM",
                "location": "The Luminara Training Hall",
                "advisor": "Professor Solara Brightflame",
                "members": 20,
                "category": "Academic"
            },
            "elements": {
                "name": "Elementalists",
                "level": "Scholars/Advanced",
                "description": "Control of fire, water, air, and earth magic at advanced levels.",
                "meeting_time": "Every Thursday, 2:00 to 3:30 PM",
                "location": "The Starveil Forest Ground",
                "advisor": "Professor Terra Auralis",
                "members": 18,
                "category": "Academic"
            },
            "spells": {
                "name": "Duelity",
                "level": "Scholars/Advanced",
                "description": "Focus on spell-casting and combat magic",
                "meeting_time": "Every Friday, 3:00 to 4:45 PM",
                "location": "The Starveil Court",
                "advisor": "Professor Vaelor Thorne",
                "members": 18,
                "category": "Academic"
            },
            "illusion": {
                "name": "Illusionists Atelier",
                "level": "Scholars/Advanced",
                "description": "Advanced illusion creation",
                "meeting_time": "Every Thursday, 3:45 to 5:00 PM",
                "location": "The Mirage Practice Grounds",
                "advisor": "Professor Selric Voidspire",
                "members": 15,
                "category": "Academic"
            },
            "time": {
                "name": "Chronomancers",
                "level": "Elite/Master",
                "description": "Study of time magic and time manipulation.",
                "meeting_time": "Every Wednesday, 2:00 to 3:30 PM",
                "location": "The Grand Chamber",
                "advisor": "Professor Cael Tideshift",
                "members": 10,
                "category": "Academic"
            },
            "mind": {
                "name": "Dominus Cognitia",
                "level": "Elite/Master",
                "description": "Mind magic, telepathy, mental influence, memory manipulation.",
                "meeting_time": "Every Monday, 2:00 to 4:30 PM",
                "location": "The Starveil Sanctum",
                "advisor": "Professor Veylor Shade",
                "members": 8,
                "category": "Academic"
            },
            "reality": {
                "name": "Aetherial Nexus",
                "level": "Elite/Master",
                "description": "Reality-bending, spatial manipulation, teleportation, and interdimensional studies.",
                "meeting_time": "Every Wednesday, 2:00 to 5:00 PM",
                "location": "The Grand Chamber",
                "advisor": "Professor Seraphine Voidweaver",
                "members": 6,
                "category": "Academic"
            },
            "": {
                "name": "",
                "level": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            },
        
        }

def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
        Name: {info['name']}

        Level: {info['level']}

        Description: {info['description']}

        Meeting Time: {info['meeting_time']}

        Location: {info['location']}

        Advisor: {info['advisor']}

        Number of Members: {info['members']}
        
        Category: {info['category']}
            """

    display(output, target="club-info")

