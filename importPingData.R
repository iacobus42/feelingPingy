importPingData <- function(file) {
  # an R function to read in the ping test results
  data <- read.csv(file, header = FALSE, stringsAsFactors = FALSE, 
                   strip.white = TRUE)
  data$V3 <- gsub(x = data$V3, pattern = "[", replacement = "", fixed = TRUE)
  data$V3 <- gsub(x = data$V3, pattern = "]", replacement = "", fixed = TRUE)
  data$V3 <- as.numeric(data$V3)
  names(data) <- c("time", "targetIP", "ping")
  data
}