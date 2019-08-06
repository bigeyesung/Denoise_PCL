import pcl
import time

def main():
    mean_k = 12
    thred = 0.5
    opt = "_k"+ str(mean_k)+ "_m" + str(thred)
    prefix = "pcd/"+ opt + "/" + "PCL/"
    
    
    filename = "./pcd/Byg72.pcd"
    start_time = time.time()
    print("PCL " + filename + " :")
    p = pcl.load(filename)
    filename = filename[6:-4]
    fil = p.make_statistical_outlier_filter()
    fil.set_mean_k(mean_k)
    fil.set_std_dev_mul_thresh(thred)
    pcl.save(fil.filter(), prefix+ filename + opt + ".pcd")
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")

    filename = "./pcd/Plan3D_1st.pcd"
    start_time = time.time()
    print("PCL " + filename + " :")
    p = pcl.load(filename)
    filename = filename[6:-4]
    fil = p.make_statistical_outlier_filter()
    fil.set_mean_k(mean_k)
    fil.set_std_dev_mul_thresh(thred)
    pcl.save(fil.filter(), prefix + filename + opt + ".pcd")
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")

    filename = "./pcd/Plan3D_2nd.pcd"
    start_time = time.time()
    print("PCL " + filename + " :")
    p = pcl.load(filename)
    filename = filename[6:-4]
    fil = p.make_statistical_outlier_filter()
    fil.set_mean_k(mean_k)
    fil.set_std_dev_mul_thresh(thred)
    pcl.save(fil.filter(), prefix + filename + opt + ".pcd")
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")
   
    filename = "./pcd/Plan3D_3rd.pcd"
    start_time = time.time()
    print("PCL " + filename + " :")
    p = pcl.load(filename)
    filename = filename[6:-4]
    fil = p.make_statistical_outlier_filter()
    fil.set_mean_k(mean_k)
    fil.set_std_dev_mul_thresh(thred)
    pcl.save(fil.filter(), prefix + filename + opt + ".pcd")
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")

    filename = "./pcd/17087.pcd"
    start_time = time.time()
    print("PCL " + filename + " :")
    p = pcl.load(filename)
    filename = filename[6:-4]
    fil = p.make_statistical_outlier_filter()
    fil.set_mean_k(mean_k)
    fil.set_std_dev_mul_thresh(thred)
    pcl.save(fil.filter(), prefix + filename + opt + ".pcd")
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    print("------")

if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()', sort='time')
    main()