################################################################
#APIのためにインポート
import googlemaps
import json

#logger
from my_logger import SimpleLogger

import os
from dotenv import load_dotenv
#envのファイルを読み込む
load_dotenv()
################################################################
#グーグルマップとAPIを連携
class GoogleMapsSearcher:
    def __init__(self, api_key):
        #logger
        self.logger_setup = SimpleLogger()
        self.logger = self.logger_setup.get_logger()
        
        try:
            #APIクライアントの初期化
            #お決まり分でAPIキーを使ってねと言っている
            self.g_maps = googlemaps.Client(key=api_key)
            self.logger.info("Google Mapsのクライアントの準備に成功しました！")
        except Exception as e:
            self.logger.error(f"Google Mapsのクライアントの準備に失敗しました！\n{e}")
            #処理停止
            raise
    
    #１つ目のフロー
    #キーワードからグーグルマップの情報見つける    
    def search_place(self, keyword, region="jp", language="ja", limit= 5):
        #地域：日本、言語：日本語、取得件数：●件
        self.logger.info(f"検索します：'{keyword}' (Region: {region}, Lang: {language}, Limit: {limit})")
        try:
            #Google Mapsにこのキーワードで検索して！
            places_result = self.g_maps.places(query=keyword, region=region, language=language)
            #status には、検索の結果に応じて色々な値が入る
            #成功の確認をしてからデータを取りに行くようにする
            if places_result['status'] == "OK":
                results = places_result['results'][:limit]
                self.logger.info(f"キーワード'{keyword}'で{len(results)}件の検索結果が見つかりました")
                return results
            else:
                self.logger.warning(f"キーワード '{keyword}' の検索結果が見つかりませんでした。ステータス: {places_result['status']}")
                #空っぽのリストを返す
                return []
        except Exception as e:
            self.logger.error(f"キーワード '{keyword}' の検索中にエラーが発生しました: \n{e}")
            #処理停止
            raise
        
    #２つ目のフロー
    #詳細情報を取得する
    def get_place_date(self, place_id, language = "ja"):
        #Place IDから場所の詳細情報を取得する
        try:
            fields = [
                "name", "formatted_address", "formatted_phone_number",
                "website", "rating", "user_ratings_total", "reviews"
                ]
            #APIを使って少佐情報を取得する
            details_result = self.g_maps.place(place_id=place_id, language=language, fields=fields)
            if details_result['status'] == "OK":
                return details_result['result']
            else:
                self.logger.warning(f"詳細情報が見つかりませんでした。ステータス: {details_result['status']}")
                #なければ処理は止めずに情報なしで返してという意味
                return None
        except Exception as e:
            self.logger.error(f"Place ID: {place_id} の詳細情報取得中にエラーが発生しました: \n{e}")
            #なければ処理は止めずに情報なしで返してという意味
            return None
        
    #３つ目のフロー
    #出力するときの詳細を最初から設定しておく
    def print_place_info(self, details):
        #情報がない場合
        if not details:
            print("表示するデータがありません")
            return
        print(f"名前: {details.get('name', '---')}")
        print(f"住所: {details.get('formatted_address', '---')}")
        print(f"電話: {details.get('formatted_phone_number', '---')}")
        print(f"URL: {details.get('website', '---')}")
        print(f"総合評価: {details.get('rating', '-')} ({details.get('user_ratings_total', 0)}件のレビュー)")
        
        #もしレビューというキーがあったら
        if 'reviews' in details:
            print("\n--- 最新の口コミ (最大5件) ---")
            #ループ処理でレビューを5件とりだす
            limit = 5
            for review in details['reviews'][:limit]:
                #本文を取り出す、なければ空白、.replace('\n', ' ')は改行をスペースに変更
                text = review.get("text", "").replace('\n', " ")
                if not text:
                    #コメントがなければ飛ばす
                    continue
                #表示する
                print(f"・{text}")
        print("-" * 40)
                
            
        


#===================================================================
#実行する
#===================================================================
if __name__ == "__main__":
    API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
    
    #インスタンス作成
    google_map_searcher = GoogleMapsSearcher(API_KEY)
    
    #１つ目：検索
    keyword = "福岡 博多区 ケーキ屋"
    limit = 3
    results = google_map_searcher.search_place(keyword, limit=limit)
    
    #2つ目：詳細情報取得
    for place in results:
        place_id = place.get("place_id")
        details = google_map_searcher.get_place_date(place_id)
        google_map_searcher.print_place_info(details)