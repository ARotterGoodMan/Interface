package com.example.api.entity.home.homedata2.popdatas;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.example.api.entity.home.homedata2.popdatas.popdataslist.DataPage4list;
import com.example.api.entity.home.homedata2.publicdata.PublicDatas;

import java.util.LinkedHashMap;

public class DataPage4 {
    JSONObject data = new JSONObject(new LinkedHashMap());
    JSONObject datas = new JSONObject(new LinkedHashMap());
    JSONObject filter = new JSONObject();
    JSONArray list = new JSONArray();
    JSONObject param = new JSONObject(new LinkedHashMap());

    public void setData() {
        this.data.put("cpc_offset",0);
        PublicDatas publicDatas = new PublicDatas();
        publicDatas.setFilterList();
        setFilter(publicDatas.getFilterList());
        this.data.put("filter",getFilter());
        this.data.put("isEnd",false);
        DataPage4list dataPage4list = new DataPage4list();
        dataPage4list.setList0();
        dataPage4list.setLists();
        setList(dataPage4list.getLists());
        this.data.put("list",getList());
        this.data.put("page", 4);
        setParam();
        this.data.put("param",getParam());
        this.data.put("ptpPartC","_mb_mls_10057922_wap-index_noab-noab");
        this.data.put("sort","pop");
        this.data.put("title","美丽说wap首页");
        this.data.put("total",40935);


    }

    public void setDatas() {
        setData();
        this.datas.put("data",getData());
        this.datas.put("returnCode",1001);
        this.datas.put("returnMessage",null);
        this.datas.put("success",true);
    }


    public JSONObject getData() {
        return data;
    }

    public void setFilter(JSONArray jsonArray) {
        this.filter.put("list",jsonArray);
    }

    public void setList(JSONObject[] jsonObjects) {
        for (int i=0;i<jsonObjects.length;i++){
            this.list.add(i,jsonObjects[i]);
        }
    }

    public void setParam() {
        this.param.put("_mgjuuid","977bbfe1-f9ab-4f86-a905-914889777c3e");
        this.param.put("cKey","wap-index");
        this.param.put("cpcEventId",70005);
        this.param.put("cpc_offset",0);
        this.param.put("eventId",70003);
        this.param.put("fcid",10057922);
        this.param.put("page",4);
        this.param.put("ptpPartC","_mb_mls_10057922_wap-index_noab-noab");
        this.param.put("ptpWallCpc","_wall_cpc");
        this.param.put("ptpWallDoc","_wall_docs");
        this.param.put("section",0);
        this.param.put("sort","pop");

    }

    public JSONArray getList() {
        return list;
    }

    public JSONObject getDatas() {
        return datas;
    }

    public JSONObject getFilter() {
        return filter;
    }

    public JSONObject getParam() {
        return param;
    }
}
