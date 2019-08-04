$(function () {
    $("#serverDropdown").on("change", function () {
        switch ($(this).val()) {
        	case "0":
                $("#serverText").html("Select a server in the dropdown to see details here.");
                break;
            case "1":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.7.10.html\">Forge Modloader 1.7.10</a>";
            			var modslink = "<a href=\"https://drive.google.com/open?id=1LsWumfkbwimx8a58t6UnC64iyqjzQKZj\">Mods</a>";
            			return "Server originally run by Rory.  Runs on Minecraft 1.7.10.<br>" +
							"Requires the following: " + forgelink + ", " + modslink;
            		}
            		)
                break;
            case "2":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://www.curseforge.com/minecraft/modpacks/roguelike-adventures-and-dungeons\">Modpack</a>";
            			return "Roguelike Adventures and Dungeons modpack.  Runs on Minecraft 1.12.2.<br>" +
							"Modpack focused on adventuring, exploration, looting, fighting.  Not so techy.<br>" +
							"Has randomly generated dungeons, 8 dimensions, RPG-style levelling and magic system, harder mobs, quests, airships, more weapons and items.<br>" +
							"If installing through Twitch launcher (easiest method) disregard following.<br>" +
							"Requires the following: " + forgelink;
            		}
            		)
                break;
			case "3":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://www.curseforge.com/minecraft/modpacks/sevtech-ages/files/2744522\">Modpack</a>"
            			return "SevTech Ages 3.1.2 modpack.  Runs on Minecraft 1.12.2.<br>" +
							"Basically a progression modpack featuring a ton of mods that you have to unlock by 'progressing' through the ages, working your way from primitive to eventually futuristic.<br>" +
							"Best move would be to play this before playing any other large modpacks, it introduces you slowly to most of the major mods.<br>" +
							"If installing through Twitch launcher (easiest method), make sure to click 'Versions' and download '3.1.2', as the default may be wrong for some, and disregard the following.<br>" +
							"Requires the following: " + forgelink;
            		}
            		)
                break;
			case "4":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://www.curseforge.com/minecraft/modpacks/ragnamod-v/files/2752080\">Modpack</a>"
            			return "Ragnamod V.  Runs on Minecraft 1.12.2.<br>" +
							"Tbh idk what this is, it's mainly used by French people, but its in English and the mod list looks amazing and its super popular.<br>" +
							"If installing through Twitch launcher (easiest method), disregard the following.<br>" +
							"Requires the following: " + forgelink;
            		}
            		)
                break;
			case "5":
            	$("#serverText").html(
            		function() {
            			var forgelink = "<a href=\"https://www.curseforge.com/minecraft/modpacks/all-the-mods-3-remix/download/2734233\">Modpack</a>"
            			return "All the Mods - Remix version 1.3.2.  Runs on Minecraft 1.12.2.<br>" +
							"Large pack with tons of mods.  Includes MineColonies for making your own medieval city and defending it (really in-depth, customization, etc.).<br>" +
							"If installing through Twitch launcher (easiest method), make sure to click 'Versions' and download '1.3.2', and disregard the following.<br>" +
							"Requires the following: " + forgelink;
            		}
            		)
                break;
        }
    });
});