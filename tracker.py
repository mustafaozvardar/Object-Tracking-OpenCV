import math

class EuclideanDistTracker:
    def __init__(self):
        self.center_points = {}  # Nesnelerin ID ve merkez noktalarını tutar
        self.id_count = 0  # ID sayacı
        self.memory = {}  # Nesnelerin kaybolma anını tutar
        self.max_disappeared = 50  # Nesne kaybolduktan sonra kaç kare boyunca beklenir

    def update(self, objects_rect):
        objects_bbs_ids = []

        # Yeni nesneler için merkez noktaları hesapla
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Tespit edilen nesnelerle eski merkez noktalarını karşılaştır
            same_object_detected = False
            for id, pt in list(self.center_points.items()):
                dist = math.hypot(cx - pt[0], cy - pt[1])

                # Aynı nesne olarak değerlendiriliyorsa, ID'yi güncelle
                if dist < 40:  # Buradaki mesafe eşiği ayarlandı
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    self.memory[id] = 0  # Nesne yeniden tespit edildiğinde hafızayı sıfırla
                    break

            # Yeni nesne tespiti (Eğer aynı nesne bulunmadıysa)
            if not same_object_detected:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.memory[self.id_count] = 0
                self.id_count += 1

        # Hafızayı güncelle ve kaybolan nesneleri sil
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            new_center_points[object_id] = self.center_points[object_id]

        self.center_points = new_center_points

        # Hafızadaki nesneleri kontrol et
        disappeared_ids = []
        for object_id in list(self.memory.keys()):
            self.memory[object_id] += 1
            if self.memory[object_id] > self.max_disappeared:
                disappeared_ids.append(object_id)

        for object_id in disappeared_ids:
            self.memory.pop(object_id)
            self.center_points.pop(object_id, None)

        return objects_bbs_ids
