import random

def generate_discord_links(num_links):
    links = []
    for i in range(num_links):
        link = 'https://discord.gg/' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
        links.append(link)
    
    with open('output.txt', 'w') as file:
        for link in links:
            file.write(link + '\n')
    
    return links

num_links = int(input('How many Discord links would you like to generate? '))
links = generate_discord_links(num_links)
print(f'{num_links} Discord links have been generated and saved to output.txt')
