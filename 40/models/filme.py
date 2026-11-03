from sqlalchemy import Column, Integer, String, Date, Text, and_
from sqlalchemy.orm import relationship
from conn import Base
from models.avaliacao import Avaliacao

class Filme(Base):

    __tablename__ = "FILME"

    id = Column("IDFILME", Integer, primary_key=True)
    titulo = Column("TITULO", String(200))
    descricao = Column("DESCRICAO", Text)
    descricao_breve = Column("DESCRICAO_BREVE", String(100))
    data_estreia = Column("DATA_ESTREIA", Date)
    url_poster = Column("URL_POSTER", String(200))

    #relacionamento 
    avaliacoes = relationship("Avaliacao",
                              primaryjoin=lambda: and_(Filme.id == Avaliacao.filme_id, Avaliacao.check_ofensivo == "N"),
                              back_populates="filme")

    #campos calculados
    @property
    def nota_media(self):
        media = 0
        if self.avaliacoes:
            soma_nota = sum(a.nota for a in self.avaliacoes)
            quantidade = len(self.avaliacoes)
            media = round(soma_nota / quantidade, 1)
        return media

    @property
    def quantidade_comentarios(self):
        return len(self.avaliacoes)

    def to_print(self, hierarquia=False):

        if hierarquia:
            avaliacoes = [avaliacao.to_print(hierarquia=False) for avaliacao in self.avaliacoes]
        else:
            avaliacoes = []

        #formatando a data de estreia para exibição
        data_estreia2 = (self.data_estreia.strftime("%d/%m/%Y %H:%M:%S") if self.data_estreia else None)
            
        return {"id": self.id
                , "titulo": self.titulo
                , "descricao": self.descricao
                , "descricao_breve": self.descricao_breve
                , "data_estreia": self.data_estreia
                , "data_estreia2": data_estreia2
                , "url_poster": self.url_poster
                , "quantidade_comentarios": self.quantidade_comentarios
                , "nota_media": self.nota_media
                , "avaliacoes": avaliacoes
                }