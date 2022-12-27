import tweepy

# config.py: accessing api key constants
import config


def about_me(api_client):
    """Print information about the client's user."""
    # The `public_metrics` addition will give me my followers count, among other things
    user = api_client.get_me(user_fields=["public_metrics"])
    print(f"My name: {user.data.name}")
    print(f"My handle: @{user.data.username}")
    print(f"My followers count: {user.data.public_metrics['followers_count']}")


def get_ztm_tweets(api_client):
    """Return a list of latest ZTM tweets"""
    ztm = api_client.get_user(username="zerotomasteryio")
    response = api_client.get_users_tweets(ztm.data.id)
    return response.data


if __name__ == "__main__":
    # Creating session to access API
    client = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_SECRET,
    )

    print("=== About Me ===")
    about_me(client)
    print()
    print("=== ZTM Tweets ===")
    for tweet in get_ztm_tweets(client):
        print(tweet, end="\n\n")
