import pdal
import time

json_s = """{

     "pipeline":[
        "./las/Byg72.las",
        {
        "type":"filters.mad",
        "dimension": "X", 
        "k":2
        },
        "./las/Byg72_mad.las"
    ]
}"""
print(json_s)
#pipeline = pdal.Pipeline(json_s)
#count = pipeline.execute()

json_s = """{

     "pipeline":[
        "./las/Byg72_mad.las",
        {
        "type":"filters.mad",
        "dimension": "Y", 
        "k":2
        },
        "./las/Byg72_mad.las"
    ]
}"""
#pipeline = pdal.Pipeline(json_s)
#count = pipeline.execute()

json_s = """{

     "pipeline":[
        "./las/Byg72_mad.las",
        {
        "type":"filters.mad",
        "dimension": "Z", 
        "k":2
        },
        "./las/Byg72_mad.las"
    ]
}"""
#pipeline = pdal.Pipeline(json_s)
#count = pipeline.execute()

json_s = """{

     "pipeline":[
        "./test.pcd",
        {
        "type":"filters.outlier",
        "method":"statistical",
        "mean_k":12,
        "multiplier":0.5
        },
        {
        "type":"filters.range",
        "limits":"Classification![7:7]"
        },
        "./test2.pcd"
    ]
}"""
start_time = time.time()
pipeline = pdal.Pipeline(json_s)
count = pipeline.execute()
elapsed_time = time.time() - start_time
print("pdal Byg72")
print(elapsed_time)
print("------")


json_s = """{

     "pipeline":[
        "./las/Plan3D_1st.las",
        {
        "type":"filters.outlier",
        "method":"statistical",
        "mean_k":12,
        "multiplier":0.5
        },
        {
        "type":"filters.range",
        "limits":"Classification![7:7]"
        },
        "Plan3D_1st_k12_m0.5.las"
    ]
}"""
start_time = time.time()
pipeline = pdal.Pipeline(json_s)
count = pipeline.execute()
elapsed_time = time.time() - start_time
print("pdal Plan3D_1st")
print(elapsed_time)
print("------")

json_s = """{

     "pipeline":[
        "./las/Plan3D_2nd.las",
        {
        "type":"filters.outlier",
        "method":"statistical",
        "mean_k":12,
        "multiplier":0.5
        },
        {
        "type":"filters.range",
        "limits":"Classification![7:7]"
        },
        "Plan3D_2nd_k12_m0.5.las"
    ]
}"""
start_time = time.time()
pipeline = pdal.Pipeline(json_s)
count = pipeline.execute()
elapsed_time = time.time() - start_time
print("pdal Plan3D_2nd")
print(elapsed_time)
print("------")

json_s = """{

     "pipeline":[
        "./las/Plan3D_3rd.las",
        {
        "type":"filters.outlier",
        "method":"statistical",
        "mean_k":12,
        "multiplier":0.5
        },
        {
        "type":"filters.range",
        "limits":"Classification![7:7]"
        },
        "Plan3D_3rd_k12_m0.5.las"
    ]
}"""
start_time = time.time()
pipeline = pdal.Pipeline(json_s)
count = pipeline.execute()
elapsed_time = time.time() - start_time
print("pdal Plan3D_3rd")
print(elapsed_time)
print("------")

json_s = """{

     "pipeline":[
        "./las/Maltby17087.las",
        {
        "type":"filters.outlier",
        "method":"statistical",
        "mean_k":12,
        "multiplier":0.5
        },
        {
        "type":"filters.range",
        "limits":"Classification![7:7]"
        },
        "Maltby17087_k12_m0.5.las"
    ]
}"""
start_time = time.time()
pipeline = pdal.Pipeline(json_s)
count = pipeline.execute()
elapsed_time = time.time() - start_time
print("pdal Maltby17087")
print(elapsed_time)
print("------")



json_s2 = """{

     "pipeline":[
        "Byg72.las",
        {
        "type":"filters.range",
        "limits":"X[0:146]"
        },
        {
        "type":"writers.las",
        "filename":"Byg72_opt_range.las"
        }

    ]
}"""



##pipeline = pdal.Pipeline(json_s2)
##count = pipeline.execute()
print("done Denoise")