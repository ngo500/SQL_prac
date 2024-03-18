--dataset source:
--https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am/about_data
--data set used under Public Domain and Dedication License
--https://opendatacommons.org/licenses/pddl/1-0/

-- select everything
SELECT * FROM FilmLocations;

-- select all film names, director names, writer names
SELECT Title, Director, Writer FROM FilmLocations;

-- select all film names, release years, and locations
-- where the release year is 2001 and newer
SELECT Title, ReleaseYear, Locations FROM FilmLocations WHERE ReleaseYear>=2001;

-- select all fun facts and locations
SELECT FunFacts, Locations FROM FilmLocations;

-- select all film names, release years, and locations
-- where the release year is 2000 and older
SELECT Title, ReleaseYear, Locations FROM FilmLocations WHERE ReleaseYear <= 2000;

-- select all film names, production company names, locations, and release years
-- where James Cameron was not a writer
SELECT Title, ProductionCompany, Locations, ReleaseYear FROM FilmLocations WHERE Writer <> "James Cameron";
