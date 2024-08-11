MODRINTH_API_URL = "https://api.modrinth.com/v2"
MOD_LIST = [
    # base mods
    "fabric-api",
    "cloth-config",
    "sodium",
    "nvidium",
    "lithium",
    "indium",
    "ferrite-core",
    "immediatelyfast",
    "modernfix",
    "moreculling",
    "ebe",

    # optional
    "sodium-extra",
    "iris",
    "debugify",
    "language-reload",
    "betterf3",

    # optifine replacements
    "animatica",
    "optigui",
    "ryoamiclights",
    "fabricbettergrass",
    "capes",
    "ok-zoomer",
    "continuity",
    "entitytexturefeatures",
    "entity-model-features",
    "polytone",
    "puzzle"
    # Add more mod slugs as needed
]
MINECRAFT_VERSIONS = [
    "1.21.1",
    "1.21",
    "1.20.6",
    "1.20.5",
    "1.20.4",
    "1.20.3",
    "1.20.2",
    "1.20.1",
    "1.20",
    "1.19.4",
    "1.19.3",
    "1.19.2",
    "1.19.1",
    "1.19",
    "1.18.2",
    "1.18.1",
    "1.18",
    "1.17.1",
    "1.17",
    "1.16.5"
    # Add more versions as needed
]
MINECRAFT_VERSION = MINECRAFT_VERSIONS[0]  # Default to the first version in the list
FABRIC_VERSION = "0.15.11"  # Update this to the latest Fabric version
FABRIC_INSTALLER_URL = "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.1/fabric-installer-1.0.1.jar"