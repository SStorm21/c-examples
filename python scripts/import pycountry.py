import pycountry
import phonenumbers
def uknowncontry():

    def get_country_code(country_name):
        # Find the country using pycountry
        country = pycountry.countries.get(name=country_name)
        if not country:
            return None
        
        # Get the country code using the phonenumbers library
        country_code = phonenumbers.country_code_for_region(country.alpha_2)
        return country_code

    # Example usage
    country_name = input('conrty name>')
    country_code = get_country_code(country_name)
    if country_code:
        print(f"The phone number code for {country_name} is +{country_code}.")
    else:
        print(f"Country code for {country_name} not found.")
