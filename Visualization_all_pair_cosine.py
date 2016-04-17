import json
import matplotlib.pyplot as plt
import numpy as np

cluster_info_file = open("pepperfry_mean_vecotor_mar_03_with_source.json","r")

def getInfoMean(seed,cluster_info_file):
	cluster_info_file_inside = open("pepperfry_mean_vecotor_mar_03_with_source.json","r")	
	final_position = []	
	urlh = []
	title = []
	source = []
	can_angle = []
	can_dist = []
	mean_simi = []

	for each in cluster_info_file_inside:
		cluster_info = json.loads(each)
		if (seed == cluster_info.keys()[0]):
			# print "Match"
			final_position = cluster_info[cluster_info.keys()[0]][3]			
			urlh = cluster_info[cluster_info.keys()[0]][0]
			title = cluster_info[cluster_info.keys()[0]][1]
			source = cluster_info[cluster_info.keys()[0]][2]			
			can_angle  = cluster_info[cluster_info.keys()[0]][5]
			can_dist = cluster_info[cluster_info.keys()[0]][6]
			mean_simi = cluster_info[cluster_info.keys()[0]][4]

	return final_position,urlh,title,source,can_angle,can_dist,mean_simi

def getInfo(seed,cluster_info_file):
	cluster_info_file_inside = open("pepperfry_mean_vecotor_mar_03_with_source.json","r")	
	final_position = []	
	cosine_similarity = []
	urlh = []
	title = []
	source = []
	all_pair_dict  = {}
	can_angle = []
	can_dist = []
	mean_simi = []
	for each in cluster_info_file_inside:
		cluster_info = json.loads(each)
		if (seed == cluster_info.keys()[0]):
			# print "Match"
			final_position = cluster_info[cluster_info.keys()[0]][5]
			cosine_similarity = cluster_info[cluster_info.keys()[0]][1]
			urlh = cluster_info[cluster_info.keys()[0]][0]
			title = cluster_info[cluster_info.keys()[0]][2]
			source = cluster_info[cluster_info.keys()[0]][3]
			all_pair_dict = cluster_info[cluster_info.keys()[0]][6]
			can_angle  = cluster_info[cluster_info.keys()[0]][7]
			can_dist = cluster_info[cluster_info.keys()[0]][8]
			mean_simi = cluster_info[cluster_info.keys()[0]][9]
	return final_position,cosine_similarity,urlh,title,source,all_pair_dict,can_angle,can_dist,mean_simi


r_out = open("input_for_r_pepperfry_mean_vector_simi_mar_04.json","w")

for idx,line in enumerate(cluster_info_file):
	bundle = json.loads(line)
	seed = bundle.keys()[0]
	print idx

	
	# final_position,cosine_similarity,urlh,title,source,all_pair_dict,angle,dist,mean_simi = getInfo(seed,cluster_info_file)
	final_position,urlh,title,source,can_angle,can_dist,mean_simi = getInfoMean(seed,cluster_info_file)
	
	r = {}
	r["fp"] = ["seed"] + final_position
	r["ms"] = [1] + mean_simi
	r["title"] = ["Mean_vector"] + title
	r["source"] = ["TP_clustering"] + source
	r["mean_angle"] = [0] + can_angle
	r["mean_dist"] = [0] + can_dist


	r_out.write(json.dumps(r)+ "\n")
				
