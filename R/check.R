library("e1071")

# Genero
train_ge <- read.table("../data/train_ge", quote="\"")
test_ge <- read.table("../data/test_ge", quote="\"")

model_ge <- naiveBayes(V1 ~ ., data = train_ge)
pred_ge <- predict(model_ge, test_ge[,2:length(test_ge)])

accuracy_ge <- sum(diag(table(pred_ge, test_ge[,1]))) / length(test_ge[,1])
accuracy_ge

# Pais
train_co <- read.table("../data/train_co", quote="\"")
test_co <- read.table("../data/test_co", quote="\"")

model_co <- naiveBayes(V1 ~ ., data = train_co)
pred_co <- predict(model_co, test_co[,2:length(test_co)])

accuracy_co <- sum(diag(table(pred_co, test_co[,1]))) / length(test_co[,1])
accuracy_co














train <- train_ge[,1001:length(train_ge)]
train <- cbind(train_ge[,1], train)

colnames(train)[1] <- "clase"

test <- test_ge[,1001:length(test_ge)]
test <- cbind(test_ge[,1], test)


model <- naiveBayes(clase ~ ., data = train)
pred <- predict(model, test[,2:length(test)])

accuracy <- sum(diag(table(pred, test[,1]))) / length(test[,1])
accuracy
