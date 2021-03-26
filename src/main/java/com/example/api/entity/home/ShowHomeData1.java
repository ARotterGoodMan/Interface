package com.example.api.entity.home;

import com.alibaba.fastjson.JSONObject;
import com.example.api.entity.home.homedata1.BannerData;
import com.example.api.entity.home.homedata1.DKeywordData;
import com.example.api.entity.home.homedata1.KeywordsData;
import com.example.api.entity.home.homedata1.RecommendData;


/**
 * @author 邵潇遥
 * @Classname Data
 * @Description TODO
 * @Date 2020/11/10 19:22
 * @Created by 邵潇遥
 * <p>
 * 用于返回数据到客户端
 */
public class ShowHomeData1 {
    JSONObject[] bannerlist = new JSONObject[4];
    JSONObject[] dKeywordlist = new JSONObject[1];
    JSONObject[] Keywordslist = new JSONObject[8];
    JSONObject[] recommendlist = new JSONObject[4];

    public JSONObject[] setBannerlist() {
        BannerData bannerData = new BannerData();
        bannerData.setBannerData0();
        bannerData.setBannerData1();
        bannerData.setBannerData2();
        bannerData.setBannerData3();
        this.bannerlist[0] = bannerData.getBannerData0();
        this.bannerlist[1] = bannerData.getBannerData1();
        this.bannerlist[2] = bannerData.getBannerData2();
        this.bannerlist[3] = bannerData.getBannerData3();
        return this.bannerlist;
    }

    public JSONObject[] setdKeywordlist() {
        DKeywordData dKeywordData = new DKeywordData();
        dKeywordData.setDKeywordData0();
        this.dKeywordlist[0] = dKeywordData.getDKeywordData0();
        return this.dKeywordlist;
    }

    public JSONObject[] setKeywordslist() {
        KeywordsData keywordsData = new KeywordsData();
        keywordsData.setKeywordsData0();
        keywordsData.setKeywordsData1();
        keywordsData.setKeywordsData2();
        keywordsData.setKeywordsData3();
        keywordsData.setKeywordsData4();
        keywordsData.setKeywordsData5();
        keywordsData.setKeywordsData6();
        keywordsData.setKeywordsData7();
        this.Keywordslist[0] = keywordsData.getKeywordsData0();
        this.Keywordslist[1] = keywordsData.getKeywordsData1();
        this.Keywordslist[2] = keywordsData.getKeywordsData2();
        this.Keywordslist[3] = keywordsData.getKeywordsData3();
        this.Keywordslist[4] = keywordsData.getKeywordsData4();
        this.Keywordslist[5] = keywordsData.getKeywordsData5();
        this.Keywordslist[6] = keywordsData.getKeywordsData6();
        this.Keywordslist[7] = keywordsData.getKeywordsData7();
        return this.Keywordslist;
    }

    public JSONObject[] setRecommendlist() {
        RecommendData recommendData = new RecommendData();
        recommendData.setRecommendData0();
        recommendData.setRecommendData1();
        recommendData.setRecommendData2();
        recommendData.setRecommendData3();
        this.recommendlist[0] = recommendData.getRecommendData0();
        this.recommendlist[1] = recommendData.getRecommendData1();
        this.recommendlist[2] = recommendData.getRecommendData2();
        this.recommendlist[3] = recommendData.getRecommendData3();
        return this.recommendlist;
    }
}
