import json
import random


def load_shows(filename="shows.json"):
    with open(filename, "r") as file:
        return json.load(file)


def get_unwatched_episodes(show_data):
    return [episode for episode in show_data["episodes"] if not episode["watched"]]


def shuffle_episode(show_data):
    unwatched = get_unwatched_episodes(show_data)

    if not unwatched:
        print("No unwatched episodes left!")
        return

    episode = random.choice(unwatched)

    print("\nYour recommended episode:")
    print(f'Show: {show_data["show"]}')
    print(f'Season {episode["season"]}, Episode {episode["episode"]}')
    print(f'Title: {episode["title"]}')
    print(f'Summary: {episode["summary"]}')


def mark_episode_watched(show_data, season_num, episode_num):
    for episode in show_data["episodes"]:
        if episode["season"] == season_num and episode["episode"] == episode_num:
            episode["watched"] = True
            return True
    return False


def save_shows(data, filename="shows.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


def main():
    data = load_shows()

    print("Available shows:")
    for i, show in enumerate(data, start=1):
        print(f"{i}. {show['show']}")

    choice = int(input("\nPick a show number: ")) - 1
    selected_show = data[choice]

    shuffle_episode(selected_show)

    mark = input("\nDo you want to mark an episode as watched? (yes/no): ").strip().lower()
    if mark == "yes":
        season = int(input("Season number: "))
        episode = int(input("Episode number: "))

        if mark_episode_watched(selected_show, season, episode):
            save_shows(data)
            print("Episode marked as watched.")
        else:
            print("Episode not found.")


if __name__ == "__main__":
    main()