import instaloader


def get_hashtag_posts(tag):
    l = instaloader.Instaloader()
    posts = l.get_hashtag_posts(tag)
    post = next(posts)
    return { "profile": post.profile, "caption": post.caption, "url": post.url }

def get_user_posts(username, num_of_posts=1):
    l = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(l.context, username)
    result = []
    posts = profile.get_posts()
    for i in range(num_of_posts):
        post = next(posts)
        while post.is_video:
            print('is video')
            post = next(posts)
        result.append(post)
    return result


# print(get_user_posts('nature', 3))