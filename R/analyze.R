
readFile <- function(path) {
  lines <- readLines(path)
  lines <- gsub(":::", ";", lines)
  lines <- read.table(text = lines, sep = ";", header = F)
  colnames(lines) <- c("id", "country", "gender")
  
  return (lines)
}

train <- readFile("../data/training.txt")
test <- readFile("../data/test.txt")
  
data <- rbind(train, test)


table(data$country)
table(train$country)
table(test$country)

table(data$gender)
table(train$gender)
table(test$gender)

table(data$gender, data$country)
table(train$gender, train$country)
table(test$gender, test$country)