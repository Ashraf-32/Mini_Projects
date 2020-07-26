class Art:
    def __init__(self, artist, title, owner, medium, year):
        self.artist = artist
        self.title = title
        self.owner = owner
        self.medium = medium
        self.year = year

    def __repr__(self):
        return f'{self.artist}. "{self.title}". {self.year}, {self.medium} {self.owner.name}, {self.owner.location}.'


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, rmv_listing):
        self.listings.remove(rmv_listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                art_listing = listing
                break
            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f"{self.art.title}, {self.price}"


veneer = Marketplace()

edytta = Client("Edytta Halpirt", "Personal collection", False)

moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art(
    "Picasso, Pablo",
    "Girl with a Mandolin (Fanny Tellier)",
    edytta,
    "oil on canvas",
    1910,
)

print(girl_with_mandolin)

# purchase = Marketplace()

edytta.sell_artwork(girl_with_mandolin, "6M (USD)")

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

veneer.show_listings()
