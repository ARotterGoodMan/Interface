package com.example.api.entity.home;

import com.alibaba.fastjson.*;
import java.util.*;

public class SetHomeData1 {
    private final JSONObject datas = new JSONObject(new LinkedHashMap());
    private final JSONObject data = new JSONObject(new LinkedHashMap());
    private final JSONObject banner = new JSONObject();
    private final JSONObject dKeyword = new JSONObject();
    private final JSONObject Keywords = new JSONObject();
    private final JSONObject recommend = new JSONObject();
    private final JSONObject context = new JSONObject();

    public void setContext() {
        this.context.put("currentTime", "1001010011");
    }

    public JSONObject read() {
        setContext();
        this.banner.put("context", context);
        this.dKeyword.put("context", context);
        this.Keywords.put("context", context);
        this.recommend.put("context", context);
        this.data.put("banner", banner);
        this.data.put("dKeyword", dKeyword);
        this.data.put("Keywords", Keywords);
        this.data.put("recommend", recommend);
        this.datas.put("data", data);
        this.datas.put("returnCode","SUCCESS");
        this.datas.put("success",true);
        return this.datas;
    }

    public void setBanner(JSONObject[] list) {
        JSONArray list1 = new JSONArray();
        for (int i=0;i<list.length;i++){
            list1.add(i, list[i]);
        }
        this.banner.put("list", list1);
    }

    public void setdKeyword(JSONObject[] list) {
        JSONArray list2 = new JSONArray();
        for (int i=0;i<list.length;i++){
            list2.add(i, list[i]);
        }
        this.dKeyword.put("list", list2);
    }

    public void setKeywords(JSONObject[] list) {
        JSONArray list3 = new JSONArray();
        for (int i=0;i<list.length;i++){
            list3.add(i, list[i]);
        }
        this.Keywords.put("list", list3);
    }

    public void setRecommend(JSONObject[] list) {
        JSONArray list4 = new JSONArray();
        for (int i=0;i<list.length;i++){
            list4.add(i, list[i]);
        }
        this.recommend.put("list", list4);
    }
}
