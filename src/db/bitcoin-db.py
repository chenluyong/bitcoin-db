import sqlite3



db = sqlite3.connect("bitcoin.db")
db.execute("""create table bitcoin_block
(
   height_id            int                            not null,
   block_hash           varchar(64)                    not null,
   pre_id               varchar(64)                    not null,
   tx_merkle_root       varchar(64)                    not null,
   bits                 varchar(64)                    not null,
   version              int                            not null,
   tx_count             int                            not null,
   size                 int                            not null,
   nonce                bigint                         not null,
   difficulty           double precision               not null,
   block_time           datetime                       not null
);
""")

db.execute("""
create table bitcoin_transaction
(
   tx_id                int                            not null,
   block_hash           varchar(64)                    not null,
   tx_hash              varchar(64)                    not null,
   version              int                            not null,
   input_count          int                            not null,
   output_count         int                            not null,
   total_out_amount     bigint                         not null,
   total_in_amount      bigint                         not null,
   tx_fee               bigint                         not null,
   is_coinbase          bit                            not null,
   is_height_lock       bit                            not null,
   is_time_lock         bit                            not null,
   lock_time            int                            not null,
   size                 int                            not null,
   tx_time              datetime                       not null,
   constraint PK_交易 primary key (tx_id)
);
""")

db.execute("""
create table bitcoin_out
(
   tx_id                int                            not null,
   idx                  int                            not null,
   amount               bigint                         not null,
   script_pubkey_len    int                            not null,
   script_pubkey        text                           not null,
   address              varchar(58)                    not null,
   is_spent             bit                            not null
);
""")

db.execute("""
create table bitcoin_in
(
   tx_id                int                            not null,
   idx                  int                            not null,
   amount               bigint                         not null,
   prev_out_txid        varchar(64)                    not null,
   prev_out_index       int                            not null,
   payment_script_length int                            not null,
   payment_script       text                           not null,
   address              varchar(58)                    not null,
   constraint PK_交易输入 primary key (tx_id, idx)
);""")