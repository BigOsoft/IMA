# IMA - INTELLIGENT MEDICAL ASSISTANT

## Introduction
Originally based on my research paper IRMI (Intelligent Remote Medical Imaging), many patients die every year due to lack of treatment or error in diagnosis of a certain disease. Developing an artificial intelligence based detection system can help in early diagnosis and treatment of many diseases.
Hereafter, I present a potential approach to having a collection of disease detection mechanisms using deep learning which utilize medical imaging for classification. To demonstrate this experiment I use two of the most major diseases detectable using medical imaging: Tuberculosis (TB) and Breast Cancer.
I have used CNN architecture and compared the performance of the network using three different activation functions. In the case of Breast Cancer, I used the INbreast dataset which has a total of 115 cases (410 images) of which 90 cases are from women with both breasts (4 images per case) and 25 cases are from mastectomy patients (2 images per case). Our network achieves an accuracy of 94.51% in predicting the cancer in breast. In the case of TB, I used the Shenzhen dataset which has 326 normal x- rays and 336 abnormal x-rays showing various manifestations of tuberculosis. Our network achieves an accuracy of 96% in predicting TB in chest X-rays.
To further demonstrate our experiment I have created an API (Application Programming Interface) for both of our detection programs which uses the Flask framework on Python. Using an API I can utilize these detection programs in any OS (operating system), program or device which can be connected to the internet. For public consumption I’ve created a simple front-end web and mobile application based on PHP and Swift languages, respectively.

## Goals
This repository is still in its very early stages. IMA is supposed to be a collection of Artificially Inetlligent Systems which will have the ability to diagnose diseases via medical imaging (for starters). This collection of system would be employed by various hostpitals, clinic and research centres around the World for early/better diagnosis of diseases. Think of the possibilities! How many people we could help simply by giving the humanity the gift of Artificially Intelligent disease detection system. This would not be a replacement of the medical experts, rather an assisting tool. The goal here is to find support in form of funding as well as help from contributors such as Computer Scientists, Medical Practitioners, Hospitals, and Clinics etc. While the ultimatum being making this a free for use tool Worldwide. The current detection systems for Breast Cancer and Tuberculosis too need work for improvement. Therefore, I leave this repository open for contributions.

## Prerequisites

* Python (3.6)
* PyTorch (0.4.1)
* torchvision (0.2.0)
* NumPy (1.14.3)
* SciPy (1.0.0)
* H5py (2.7.1)
* imageio (2.4.1)
* pandas (0.22.0)
* tqdm (4.19.8)
* opencv-python (3.4.2)
* For TB make sure you download and place the TB model inside the TB folder from here: https://drive.google.com/drive/folders/1I3ub8CKBSYOBpHIpFmF_bPjNTKwqakjh?usp=sharing

## License

This repository is licensed under the terms of the GNU AGPLv3 license.

## How to run the code


## References

**Deep Neural Networks Improve Radiologists' Performance in Breast Cancer Screening**\
Nan Wu, Jason Phang, Jungkyu Park, Yiqiu Shen, Zhe Huang, Masha Zorin, Stanisław Jastrzębski, Thibault Févry, Joe Katsnelson, Eric Kim, Stacey Wolfson, Ujas Parikh, Sushma Gaddam, Leng Leng Young Lin, Kara Ho, Joshua D. Weinstein, Beatriu Reig, Yiming Gao, Hildegard Toth, Kristine Pysarenko, Alana Lewin, Jiyon Lee, Krystal Airola, Eralda Mema, Stephanie Chung, Esther Hwang, Naziya Samreen, S. Gene Kim, Laura Heacock, Linda Moy, Kyunghyun Cho, Krzysztof J. Geras\
IEEE Transactions on Medical Imaging\
2019

    @article{wu2019breastcancer, 
        title = {Deep Neural Networks Improve Radiologists' Performance in Breast Cancer Screening},
        author = {Nan Wu and Jason Phang and Jungkyu Park and Yiqiu Shen and Zhe Huang and Masha Zorin and Stanis\l{}aw Jastrz\k{e}bski and Thibault F\'{e}vry and Joe Katsnelson and Eric Kim and Stacey Wolfson and Ujas Parikh and Sushma Gaddam and Leng Leng Young Lin and Kara Ho and Joshua D. Weinstein and Beatriu Reig and Yiming Gao and Hildegard Toth and Kristine Pysarenko and Alana Lewin and Jiyon Lee and Krystal Airola and Eralda Mema and Stephanie Chung and Esther Hwang and Naziya Samreen and S. Gene Kim and Laura Heacock and Linda Moy and Kyunghyun Cho and Krzysztof J. Geras}, 
        journal = {IEEE Transactions on Medical Imaging},
        year = {2019}
    }
