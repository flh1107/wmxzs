1、通过xlsx2jsonl等python脚本将xlsx样本集转化成jsonl文件
2、运行generate_data.py，将每个对话重复生成100遍，用于语料训练
3、使用internlm2-chat-7b进行微调训练
配置文件internlm2_chat_7b_qlora_trade_e3.py
运行命令
xtuner train internlm2_chat_7b_qlora_trade_e3.py --deepspeed deepspeed_zero2
mkdir hf
export MKL_SERVICE_FORCE_INTEL=1
xtuner convert pth_to_hf ./internlm2_chat_7b_qlora_trade_e3.py ./work_dirs/internlm2_chat_7b_qlora_trade_e3/epoch_3.pth ./hf
xtuner convert merge ./internlm2-chat-7b ./hf ./merged --max-shard-size 2GB
运行对话
xtuner chat ./merged --prompt-template internlm_chat
