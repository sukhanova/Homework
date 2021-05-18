-- More JOIN operations: https://sqlzoo.net/wiki/More_JOIN_operations
-- 1.List the films where the yr is 1962 [Show id, title]
SELECT id, title
FROM movie
WHERE yr=1962;

-- 2.Give year of 'Citizen Kane'.

-- 3.List all of the Star Trek movies, include the id, title and yr:
-- (all of these movies include the words Star Trek in the title). Order results by year.

-- 4.What id number does the actor 'Glenn Close' have?

-- 5.What is the id of the film 'Casablanca'

-- 6.Obtain the cast list for 'Casablanca': what is a cast list?
-- Use movieid=11768, (or whatever value you got from the previous question)

-- 7.Obtain the cast list for the film 'Alien'

-- 8.List the films in which 'Harrison Ford' has appeared

-- 9.List the films where 'Harrison Ford' has appeared - but not in the starring role. 
-- [Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role]

-- 10.List the films together with the leading star for all 1962 films.