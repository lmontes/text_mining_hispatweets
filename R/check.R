library("e1071")
library("rpart")

# Cargamos los datasets
train_ge <- read.table("../data/train_ge", quote="\"")
test_ge <- read.table("../data/test_ge", quote="\"")

train_co <- read.table("../data/train_co", quote="\"")
test_co <- read.table("../data/test_co", quote="\"")


# Genero - NB con BoW (0.3368132)
model_ge <- naiveBayes(V1 ~ ., data = train_ge)
pred_ge <- predict(model_ge, test_ge[,2:length(test_ge)])

accuracy_ge <- sum(diag(table(pred_ge, test_ge[,1]))) / length(test_ge[,1])
accuracy_ge

# Genero - Arboles clasificacion con BoW (0.4802198)
model_ge <- rpart(V1 ~ ., method="class", data = train_ge)
pred_ge <- predict(model_ge, test_ge[,2:length(test_ge)], type = "class")

accuracy_ge <- sum(diag(table(pred_ge, test_ge[,1]))) / length(test_ge[,1])
accuracy_ge


# Genero - NB sin BoW (0.4005495)
train <- train_ge[,999:length(train_ge)]
train <- cbind(train_ge[,1], train)

colnames(train)[1] <- "clase"

test <- test_ge[,999:length(test_ge)]
test <- cbind(test_ge[,1], test)

model <- naiveBayes(clase ~ ., data = train)
pred <- predict(model, test[,2:length(test)])

accuracy <- sum(diag(table(pred, test[,1]))) / length(test[,1])
accuracy


# Pais - NB con BoW (0.8516484)
model_co <- naiveBayes(V1 ~ ., data = train_co)
pred_co <- predict(model_co, test_co[,2:length(test_co)])

accuracy_co <- sum(diag(table(pred_co, test_co[,1]))) / length(test_co[,1])
accuracy_co


# Pais - Arboles de clasificacion con BoW (0.8346154)
model_co <- rpart(V1 ~ ., method="class", data = train_co)
pred_co <- predict(model_co, test_co[,2:length(test_co)], type = "class")

accuracy_co <- sum(diag(table(pred_co, test_co[,1]))) / length(test_co[,1])
accuracy_co















