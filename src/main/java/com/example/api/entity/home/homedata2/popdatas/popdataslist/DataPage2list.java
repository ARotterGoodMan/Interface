package com.example.api.entity.home.homedata2.popdatas.popdataslist;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

import java.util.LinkedHashMap;

public class DataPage2list {
    JSONObject[] lists = new JSONObject[30];
    JSONObject list0 = new JSONObject(new LinkedHashMap());

    public void setList0() {
        this.list0.put("acm","3.ms.0_4_1m70y5k.0.13384-69004.s026ur4QK5gf1.t" +
                "_-sd_117-lc_16");
        this.list0.put("cfav",49);
        this.list0.put("clientUrl","http://item.meilishuo.com/h5/detail/1m70" +
                "y5k?acm=3.ms.0_4_1m70y5k.0.13384-69004.s026ur4QK5gf1.t_-sd_" +
                "117-lc_16");
        this.list0.put("cparam",null);
        this.list0.put("iid","1m70y5k");
        this.list0.put("itemMarks","1525 353 181");
        this.list0.put("itemType",10);
        this.list0.put("leftbottom_taglist",new JSONArray());
        this.list0.put("lefttop_taglist",new JSONArray());
        this.list0.put("link","http://item.meilishuo.com/h5/detail/1m70y5k?a" +
                "cm=3.ms.0_4_1m70y5k.0.13384-69004.s026ur4QK5gf1.t_-sd_117-l" +
                "c_16");
        this.list0.put("orgPrice","￥84.29");
        this.list0.put("popularStar",0);
        this.list0.put("price",59);
        this.list0.put("props",new JSONArray().add("2018秋季新款韩版百搭格子长袖" +
                "衬衫+前短后长针织气质开衫外套+高腰直筒九分牛仔裤三件套装"));
        this.list0.put("ptpC","_mb_mls_10057922_wap-index_noab-noab");
        this.list0.put("sale",4886);
        this.list0.put("shopId",10664478);
        JSONObject show = new JSONObject(new LinkedHashMap());
        show.put("h",416);
        show.put("img","http://s11.mogucdn.com/mlcdn/c45406/180808_600abce0g" +
                "8dc8i4f6ic7k27i7837l_640x960.jpg_320x999.jpg");
        show.put("w",320);
        this.list0.put("show",show);
        JSONObject showLarge = new JSONObject(new LinkedHashMap());
        showLarge.put("h",840);
        showLarge.put("img","http://s3.mogucdn.com/mlcdn/c45406/180808_600ab" +
                "ce0g8dc8i4f6ic7k27i7837l_640x960.jpg_560x999.jpg");
        showLarge.put("w",560);
        this.list0.put("shpwLarge",showLarge);
        this.list0.put("title","2018秋季新款韩版百搭格子长袖衬衫+前短后长针织气质开衫" +
                "外套+高腰直筒九分牛仔裤三件套装");
        this.list0.put("titleTags",null);
        this.list0.put("type",2);
    }

    public void setLists() {
        for (int i=0;i<this.lists.length;i++){
            lists[i] = getList0();
        }
    }

    public JSONObject getList0() {
        return list0;
    }

    public JSONObject[] getLists() {
        return lists;
    }
}
