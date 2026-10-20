from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from conn import Base

class Avaliacao(Base):

    __tablename__ = "AVALIACAO"

    id = Column("IDAVALIACAO", Integer, primary_key=True)
    data_avaliacao = Column("DATA_AVALIACAO", DateTime)
    comentario = Column("COMENTARIO", Text)
    nota = Column("NOTA", Integer)
    alerta_ofensivo = Column("ALERTA_OFENSIVO", String(1))
    check_ofensivo = Column("CHECK_OFENSIVO", String(1))

    #relacionamento 
    filme_id = Column("IDFILME", Integer, ForeignKey("FILME.IDFILME"))
    usuario_id = Column("IDUSUARIO", Integer, ForeignKey("USUARIO.IDUSUARIO"))

    # dados do relacionamento
    filme = relationship("Filme", back_populates="avaliacoes")
    usuario = relationship("Usuario")

    def to_print(self, hierarquia=False):

        if hierarquia:
            filme = self.filme.to_print()
            usuario = self.usuario.to_print()
        else:
            filme = self.filme_id
            usuario = self.usuario_id

        #formatando a data de avaliacao para exibição
        data_avaliacao2 = (self.data_avaliacao.strftime("%d/%m/%Y %H:%M:%S") if self.data_avaliacao else None)

        return {"id": self.id
                , "filme_id": self.filme_id
                , "usuario_id": self.usuario_id
                , "data_avaliacao": self.data_avaliacao
                , "data_avaliacao2": data_avaliacao2
                , "comentario": self.comentario
                , "nota": self.nota
                , "alerta_ofensivo": self.alerta_ofensivo
                , "check_ofensivo": self.check_ofensivo
                , "filme": filme
                , "usuario": usuario
            }