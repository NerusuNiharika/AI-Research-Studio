import requests

from config.settings import PEXELS_API_KEY

PEXELS_URL = "https://api.pexels.com/v1/search"


def search_image(query: str):

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    try:

        response = requests.get(
            PEXELS_URL,
            headers=headers,
            params={
                "query": query,
                "per_page": 1,
                "orientation": "landscape",
            },
            timeout=15,
        )

        response.raise_for_status()

        photos = response.json().get("photos", [])

        if not photos:
            return None

        photo = photos[0]

        return {

            "image_url": photo["src"]["large2x"],

            "source": f"Pexels • {photo['photographer']}",

            "source_url": photo["url"]

        }

    except Exception as e:

        print("Pexels Error:", e)

        return None


def attach_images(topic: str, sections: list):

    used_images = set()

    # -------------------------
    # Hero Image
    # -------------------------

    hero_query = topic

    if sections:

        first_query = sections[0].get("image_query")

        if first_query:

            hero_query = first_query

    hero = search_image(hero_query)

    if hero:

        used_images.add(hero["image_url"])

    enhanced_sections = []

    # -------------------------
    # Section Images
    # -------------------------

    for section in sections:

        title = section["title"]

        content = section["content"]

        query = section.get("image_query")

        if not query:

            query = f"{topic} {title}"

        image = search_image(query)

        if image:

            if image["image_url"] in used_images:

                image = None

            else:

                used_images.add(image["image_url"])

        enhanced_sections.append(

            {

                "title": title,

                "content": content,

                "image": image

            }

        )

    return {

        "hero": hero,

        "sections": enhanced_sections

    }