----cloud2_code_common
DELETE FROM c_order_section_info WHERE NAME LIKE '%selenium%'
----产品信息表

DELETE FROM c_order_materials_section WHERE NAME LIKE '%selenium%';
----物资信息

DELETE FROM c_purchase_main WHERE NAME LIKE '%selenium%';
----采购计划

DELETE FROM c_order_info WHERE NAME LIKE '%selenium%';
----作业单

DELETE FROM c_upload_print_codebag WHERE remark LIKE '%selenium%';
----上传码包

DELETE FROM c_upload_activate WHERE remark LIKE '%selenium%' OR remark2 LIKE '%selenium%';
----激活申请