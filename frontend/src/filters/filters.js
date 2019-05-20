function statusdesc(value)
{
    if (value===0)
        return "未开始"
    if (value===1)
        return "进行中"
    if (value===2)
        return "已完成"
    return "未知"
}

function roledesc(value)
{
    if (value)
        return "管理员"
    else
        return "普通用户"
}
export {statusdesc,roledesc}