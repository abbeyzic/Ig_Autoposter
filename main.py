from utils.twitter_fetcher import fetch_latest_tweets
from utils.summarizer import summarize_tweet
from utils.caption_generator import generate_caption
from utils.template_renderer import render_image
from utils.instagram_poster import post_to_instagram
from utils.images_host import upload_image


def run(username):
    tweets = fetch_latest_tweets(username, count=1)
    if not tweets:
        print("No tweets found.")
        return

    tweet = tweets[0]
    title, summary = summarize_tweet(tweet)
    # print("Title:", title)
    # print("Summary:", summary)

    caption = generate_caption(title, summary)
    # print("Caption:", caption)


    image_path = render_image(title, summary)
    # print("Image generated:", image_path)
    if not image_path:
        print("Failed to render image.")
        return

    image_link = upload_image(image_path)

    success = post_to_instagram(image_path, caption)
    if success:
        print("All done!")

if __name__ == "__main__":
    run("Bloomberg")

        
