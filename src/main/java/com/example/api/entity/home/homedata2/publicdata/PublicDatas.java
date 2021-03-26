package com.example.api.entity.home.homedata2.publicdata;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

import java.util.LinkedHashMap;

public class PublicDatas {
    private final JSONArray filterList = new JSONArray();
    private final JSONObject filterl0 = new JSONObject(new LinkedHashMap());
    private final JSONObject filterl1 = new JSONObject(new LinkedHashMap());
    private final JSONObject filterl2 = new JSONObject(new LinkedHashMap());


    public void setFilterList() {
        setFilterL0();
        setFilterL1();
        setFilterL2();
        this.filterList.add(0, getFilterL0());
        this.filterList.add(1, getFilterL1());
        this.filterList.add(2, getFilterL2());
    }

    public void setFilterL0() {
        filterl0.put("fcid", 10057922);
        filterl0.put("sort", "pop");
        filterl0.put("style", null);
        filterl0.put("title", "流行");
        filterl0.put("type", "sort");
    }

    public void setFilterL1() {
        filterl1.put("fcid", 10057922);
        filterl1.put("sort", "sell");
        filterl1.put("style", null);
        filterl1.put("title", "热销");
        filterl1.put("type", "sort");
    }

    public void setFilterL2() {
        filterl2.put("fcid", 10057922);
        filterl2.put("sort", "new");
        filterl2.put("style", null);
        filterl2.put("title", "上新");
        filterl2.put("type", "sort");
    }


    public JSONArray getFilterList() {
        return filterList;
    }

    public JSONObject getFilterL0() {
        return filterl0;
    }

    public JSONObject getFilterL1() {
        return filterl1;
    }

    public JSONObject getFilterL2() {
        return filterl2;
    }
}
