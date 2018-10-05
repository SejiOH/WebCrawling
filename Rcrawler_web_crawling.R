# Prerequites
library(tidyverse)
library(filesstrings)

# Create directories if there is no directory.
create_dir("F:/github_codes")
create_dir("F:/github_codes/web_crawling")

# Set a working directory.
setwd("F:/github_codes/web_crawling")
getwd()
dir()

# Create and open a source file if there is no file.
file.create("Rcrawler_web_crawling.R")
file.edit("Rcrawler_web_crawling.R")

# Directly download web pages from search results in the website
download.file("https://www.bbc.co.uk/search?q=mars+travel", "bbc_search_result.html"))

for (i in 2:10) {
i <- as.character(i)
target <- paste("https://www.bbc.co.uk/search?q=mars+travel#page=", i, sep="")
destination = paste("bbc_search_result", i, ".html", sep="")
download.file(target,destination)}

# Install and upload the package - Rcrawler
install.packages("Rcrawler")
library(Rcrawler)

# Filter and scrap web pages by the keywords 'mars' and 'travel'.
# Collect only webpages that has an accuracy percentage
# higher than 50% of matching 'mars' and 'travel'.
Rcrawler(Website="https://www.bbc.com",
KeywordsFilter = c("mars", "travel"),
KeywordsAccuracy = 50,
no_cores=4, no_conn=4)

# The directory 'bbc.com-030339' has been created.

# Or try this one to see the connection of webpages.
Rcrawler(Website="https://www.bbc.com",
KeywordsFilter = c("mars", "travel"),
KeywordsAccuracy = 50,
NetworkData = TRUE, NetwExtLinks =TRUE,
statslinks = TRUE,
no_cores=4, no_conn=4)

# The directory 'bbc.com-030455' has been created.
