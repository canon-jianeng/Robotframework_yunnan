----cloud2_code_common
DELETE FROM c_order_section_info WHERE NAME LIKE '%selenium%'
----��Ʒ��Ϣ��

DELETE FROM c_order_materials_section WHERE NAME LIKE '%selenium%';
----������Ϣ

DELETE FROM c_purchase_main WHERE NAME LIKE '%selenium%';
----�ɹ��ƻ�

DELETE FROM c_order_info WHERE NAME LIKE '%selenium%';
----��ҵ��

DELETE FROM c_upload_print_codebag WHERE remark LIKE '%selenium%';
----�ϴ����

DELETE FROM c_upload_activate WHERE remark LIKE '%selenium%' OR remark2 LIKE '%selenium%';
----��������