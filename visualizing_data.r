
library(ggplot2)
library(jsonlite)
library(rjson)
library(zoom)

read_file <- function(){
  input_file <- file("input_for_r_pepperfry_text_Feb_11_with_original_title.json","r")
  lns <- readLines(input_file,-1L)
  simi_data <- lapply(X = lns, fromJSON)
  return (simi_data)
}

visualize <- function(cnt,simi_data){
  
  length_of_seed = length(simi_data)
  final_position = head(simi_data[[cnt]])$fp
  cosine_similarity = head(simi_data[[cnt]])$cs
  title_candidates = head(simi_data[[cnt]])$title
  seed <- c(0)
  seed_vector <- rep(seed,length(cosine_similarity))
  verify = 0
  add_tracker = 0
  for (items in final_position){
    if(items=="add"){
      verify = 1 
      add_tracker <- add_tracker + 1
    }
  }
  data_frame <- data.frame(seed_vector,cosine_similarity,final_position,title_candidates)
  #print (ggplot(data_frame,aes(seed_vector,cosine_similarity),colors(final_position)) + geom_point(alpha = 0.3))
  #ans <- readline("want to see next")
  
  #print (final_position)
  print("called")
  if(verify == 1 & add_tracker > 1){
    #print(qplot(jitter(seed_vector,factor = 1.1),jitter(cosine_similarity,factor = 1.1),color = final_position,size = I(4)))
    #identify(seed_vector,cosine_similarity,labels=row.names(data_frame))
    #coords <- locator(type="l") # add lines
    #coords # display list
    print( ggplot(data_frame, aes(x= jitter(seed_vector,factor = .9), y= jitter(cosine_similarity,factor = .9), colour=final_position,label=title_candidates)) +geom_point() +geom_text(aes(label=ifelse(final_position == "add" | final_position == "dele" | final_position == "ret",as.character(title_candidates),'')),hjust=0.6, vjust=1) + guides(colour = guide_colorbar(override.aes = list(size=10))))
    
    ans <- readline("want to see next")
  }
  
}

fl = read_file()

for (i in 1:400){
  print (i)
  visualize(i,fl)
}

