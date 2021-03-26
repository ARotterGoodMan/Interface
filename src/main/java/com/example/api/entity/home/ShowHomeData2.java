package com.example.api.entity.home;


import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

import java.util.LinkedHashMap;

/**
 * @author 邵潇遥
 * @Classname Data
 * @Description TODO
 * @Date 2020/11/10 19:22
 * @Created by 邵潇遥
 * <p>
 * 用于返回数据到客户端
 */
public class ShowHomeData2 {
    private JSONObject data = new JSONObject(new LinkedHashMap());

    public void setData(JSONObject data) {
        this.data = data;
    }

    public JSONObject getData() {
        return data;
    }
}
